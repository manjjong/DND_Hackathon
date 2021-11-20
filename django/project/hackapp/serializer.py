from .models import Challenge_Check, Follow, User, Challenge, Challenge_User
from rest_framework import serializers, viewsets

# 유저 부분
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_pw', 'name')
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.user_pw = validated_data.get('user_pw', instance.user_pw)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 팔로우 부분
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('num', 'user_id', 'target_id')
    
    def create(self, validated_data):
        return Follow.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.num = validated_data.get('num', instance.num)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.target_id = validated_data.get('target_id', instance.target_id)
        instance.save()
        return instance

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

# 도전 부분
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('challenge_id', 'name', 'start_date', 'end_date', 'image', 'contents', 'creator_id')
    
    def create(self, validated_data):
        return Challenge.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.challenge_id = validated_data.get('challenge_id', instance.challenge_id)
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.start_date)
        instance.image = validated_data.get('image', instance.start_date)
        instance.contents = validated_data.get('contents', instance.start_date)
        instance.creator_id = validated_data.get('creator_id', instance.start_date)
        instance.save()
        return instance

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

# 도전유저 부분
class Challenge_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge_User
        fields = ('challenge_id', 'user_id', 'start_date', 'num')
    
    def create(self, validated_data):
        return Challenge_User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.challenge_id = validated_data.get('challenge_id', instance.challenge_id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.num = validated_data.get('num', instance.num)
        instance.save()
        return instance

class Challenge_UserViewSet(viewsets.ModelViewSet):
    queryset = Challenge_User.objects.all()
    serializer_class = Challenge_UserSerializer


# 도전체크 부분
class Challenge_CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge_Check
        fields = ('num', 'challenge_id', 'user_id', 'check_date')
    
    def create(self, validated_data):
        return Challenge_Check.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.num = validated_data.get('num', instance.num)
        instance.challenge_id = validated_data.get('challenge_id', instance.challenge_id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.check_date = validated_data.get('check_date', instance.check_date)        
        instance.save()
        return instance

class Challenge_CheckViewSet(viewsets.ModelViewSet):
    queryset = Challenge_Check.objects.all()
    serializer_class = Challenge_CheckSerializer